import os


if __name__ == '__main__':
    setup_path = os.path.join(os.path.curdir,
                              "setup.py")

    with open(setup_path, 'r') as setup_file:
        setup_content = setup_file.read()

    handlers_list_string = "'rotest.result_handlers': ["
    new_handler_string = "            '{{ cookiecutter.handler_name }} = " \
         "{{ cookiecutter.project_slug }}.{{ cookiecutter.handler_name }}." \
         "{{ cookiecutter.handler_name }}:{{ cookiecutter.handler_class_name }}',"

    setup_content = setup_content.replace(handlers_list_string,
                      handlers_list_string + os.linesep + new_handler_string)

    with open(setup_path, 'w') as setup_file:
        setup_file.write(setup_content)
