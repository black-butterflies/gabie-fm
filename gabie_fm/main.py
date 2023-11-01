import typer

existing_usernames = ["rick", "morty"]


def maybe_create_user(username: str):
    if username in existing_usernames:
        print("The user already exists")
        raise typer.Abort()
    else:
        print(f"User created: {username}")


def send_new_user_notification(username: str):
    # somehow send a notification here for the new user, maybe an email
    print(f"Notification sent for new user: {username}")


def main(username: str):
    if username == "root":
        print("The root user is reserved")
        raise typer.Exit(code=1)
    maybe_create_user(username)
    send_new_user_notification(username)


if __name__ == "__main__":
    typer.run(main)
