from Nutrin.User.Services.buscarUser import buscarUser

def excluirUser(username):
    user = buscarUser(username, True)
    if user:
        from Nutrin import db
        db.session.delete(user)
        db.session.commit()
        return True
    return False