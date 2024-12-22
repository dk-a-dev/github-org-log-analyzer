# GitHub Organization Wrapped Generator

## Overview

A GitHub Org Data Analyzer is a tool designed to analyze GitHub activity data. It provides insights into various metrics such as total active days, longest gaps, busiest days, longest streaks, month-wise activity, time-wise activity, developer activity, and repository activity based on logs of GitHub activity.

## Features

- **Total Active Days**: Calculate the total number of active days.
- **Longest Gap**: Identify the longest gap between activities.
- **Busiest Day**: Find the day with the highest number of activities.
- **Longest Streak**: Determine the longest streak of consecutive active days.
- **Month-wise Activity**: Visualize activity on a monthly basis.
- **Time-wise Activity**: Visualize activity based on the time of day.
- **Developer Activity**: Analyze the activity of individual developers.
- **Repository Activity**: Analyze the activity of repositories.

## Setup

### Prerequisites
- Get logs of your organization's using webhook created on discord through github
- use extension like Discrub to download the logs in csv format
- Setup virtual environment
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/github-data-analyzer.git
    cd github-data-analyzer
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

Warning: clean the data before uploading it to the application

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run core/ui.py
    ```
2. Open your web browser and navigate to the URL provided by Streamlit.
3. Upload a CSV file containing GitHub activity data.
4. The application will display various metrics and visualizations based on the uploaded data.

## File Structure

- `core/main.py`: Contains the core functions for data analysis.
- `core/ui.py`: Contains the Streamlit UI code.
- `config.yaml`: Configuration file for authentication.
- `README.md`: Project documentation.

## Example
https://gdsc-wrapped-2024.streamlit.app/
(Required organization logs to be uploaded, with data access perms)

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact
For any questions or feedback, please contact [Dev Keshwani](mailto:dev.keshwani345@gmail.com).
