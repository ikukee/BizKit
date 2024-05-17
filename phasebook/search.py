from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):   
    if not args: # return all users if there are no parameters
        return USERS
    else: 
        result = [];
        for user in USERS:  
            match = False # initialize a variable which can state that a user has a matching criteria or not
            for k,v in args.items(): # set match to true if a criteria is matched using key value pair
                if k == "id" and user.get("id") == v:
                    match = True 
                elif k == "name" and v.lower() in user.get(k, "").lower():
                    match = True
                elif k == "age" and user.get(k) is not None:
                    if (int(user.get(k) - 1 <= int(v) <= int(user.get(k) + 1))): # age - 1 <= age <= age + 1
                        match = True
                elif k == "occupation" and v.lower() in user.get(k, "").lower(): #
                    match = True
                if match: # checks if match is true then append user to the list
                    result.append(user)
                    break  # break to proceed to the next user from USER
        return result