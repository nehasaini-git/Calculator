from behave import given, when, then
from calculator import Calculator


@given("I have entered {number1:d} into the calculator")
def step_impl(context, number1):
    context.number1 = number1

@given("I have also entered {number2:d} into the calculator")
def step_impl(context, number2):
    context.number2 = number2

@when("I press add")
def step_impl(context):
    context.calculator = Calculator()
    context.result = context.calculator.add(context.number1, context.number2)

@then("the sum should be {result:d}")
def step_impl(context, result):
    assert context.result == result