from wrapper import *
from behave import given, then

from urls import * 
from post_data import *

@when("make get request with id {pet_id}")
def step_make_request_with_id(context, pet_id):
    context.response = make_requests("get", f"https://petstore.swagger.io/v2/pet/{pet_id}")


@when("make request to create a pet with name {pet_name}")
def step_make_request_create_pet(context, pet_name):
    url_post = url_create_pet

    data_to_use = post_data_create_pet.replace("{name}", pet_name)
    

    context.response = requests.post(url_post, data=data_to_use, headers={"Content-Type": "application/json"})


@then("response code is {expected_status:d}")
def step_check_response_code(context, expected_status):
    check_status_code(context.response, expected_status)


@when("make request to get user {username}")
def step_make_request_get_user(context, username):
    url_get_user = f"https://petstore.swagger.io/v2/user/{username}"
    context.response = make_requests("get", url_get_user)