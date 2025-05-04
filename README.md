# Blue Lagoon Project

This README provides instructions to set up a Python environment for the Blue Lagoon project and install the required dependencies.

## Setting Up the Python Environment

1. **Create a Virtual Environment**  
    Open a terminal and navigate to the project directory. Run the following command to create a virtual environment using `venv`:

    ```bash
    python -m venv venv
    ```

    This will create a folder named `venv` in your project directory.

2. **Activate the Virtual Environment**  
    - On **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - On **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```

    Once activated, your terminal prompt should indicate that the virtual environment is active.

3. **Install Dependencies**  
    With the virtual environment active, install the required dependencies from the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary packages for the project.

## Deactivating the Virtual Environment

When you're done working, deactivate the virtual environment by running:

```bash
deactivate
```

## Notes

- Ensure you have Python installed on your system. You can check by running `python --version` in your terminal.
- If `pip` is not installed, refer to the [official Python documentation](https://pip.pypa.io/en/stable/installation/) for installation instructions.

You're now ready to work on the Blue Lagoon project!