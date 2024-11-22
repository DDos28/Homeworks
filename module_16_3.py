from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Example, возраст: 18'}

@app.get('/users')
async def users_():
    return users

@app.post('/user/{username}/{age}')
async def new_user(username: str, age: int):
    next_user_id = max(int(k) for k in users.keys()) + 1 if users else 1
    users[str(next_user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {next_user_id} is registered"

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int):
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"The user {user_id} is updated"}

@app.delete('/user/{user_id}')
async def delete_user(user_id: int):
    del users[user_id]
    return {"message": f"The user {user_id} is deleted"}
