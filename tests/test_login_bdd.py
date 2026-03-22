from pytest_bdd import scenario, scenarios
from step_definitions.login_steps import *

scenarios('../features/login.feature')
