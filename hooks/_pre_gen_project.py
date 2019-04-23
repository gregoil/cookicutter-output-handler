import os

if __name__ == '__main__':
    setup_path = os.path.join(os.path.curdir,
                              "setup.py")

    assert os.path.isfile(setup_path), \
        "Not inside a project dir (can't find setup.py)"

    with open(setup_path, 'r') as setup_file:
        setup_content = setup_file.read()

    assert "'rotest.result_handlers': [" in setup_content, \
        "Can't find 'result_handlers' list in setup.py"
