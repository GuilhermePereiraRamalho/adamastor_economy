from ninja import Router
from typing import List, Optional
from django.shortcuts import get_object_or_404
from api.models.user_models import User
from api.schemas.user_schema import UserOut, UserIn, UserUpdate
from ninja.errors import HttpError

user_router = Router(tags=['Users'])

@user_router.post("/", response={201: UserOut})
def create_user(request, user_in: UserIn):
    user_data = user_in.dict()
    password = user_data.pop('password')
    user = User.objects.create(**user_data)
    user.set_password(password)
    user.save()
    return user

@user_router.get("/", response=List[UserOut])
def read_users(request):
    users = User.objects.all().order_by('id')
    return [UserOut.from_orm(user) for user in users]

@user_router.get('/{user_id}', response={200: UserOut})
def get_user_by_id(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    return UserOut.from_orm(user)

@user_router.put("/{user_id}", response=UserOut)
def update_user(request, user_id: int, data: UserUpdate):
    user = get_object_or_404(User, id=user_id)
    for attribute, value in data.dict(exclude_none=True).items():
        setattr(user, attribute, value)
    user.save()
    return user

@user_router.delete("/{user_id}", response={204: None})
def delete_user(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return None
