from behave import __main__ as behave_runner

'''
This file is alternative for running behave CLI commands from Terminal in order to run BDD test cases
'''

if __name__ == '__main__':
    features_path = 'features'
    additional_parameter = ' -f allure_behave.formatter:AllureFormatter -o allure-results '
    cli_parameters = additional_parameter + features_path
    behave_runner.main(cli_parameters)


