from fastapi import HTTPException, status, Request
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from src.user.dtos import UserSchema,LoginSchema
from src.user.models import UserModel
import jwt
from src.utils.settings import settings
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def register(body: UserSchema, db: Session):
    existing = (
        db.query(UserModel)
        .filter(
            (UserModel.username == body.username)
            | (UserModel.email == body.email)
        )
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists",
        )

    new_user = UserModel(
        name=body.name,
        username=body.username,
        hash_password=pwd_context.hash(body.password),
        email=body.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "Registration Done"}

def login_user(body:LoginSchema,db:Session):
    user=db.query(UserModel).filter(UserModel.username==body.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )
    if not pwd_context.verify(body.password, user.hash_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )
    exp_time=datetime.now() + timedelta(minutes=settings.EXP_TIME)

    token=jwt.encode({"_id": user.id, "exp": exp_time}, settings.SECRET_KEY, settings.ALGORITHM)
    return{"token":token}

def is_authenticated(request: Request, db: Session):
    token = request.headers.get("authorization")
    token = token.split(" ")[-1]
    data = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    user_id = data.get("_id")
    exp_time = data.get("exp")

    current_time = datetime.now().timestamp()
    if current_time > exp_time:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
        )
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token has expired",
                )

    return "Done"