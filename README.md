# Weather Data Pipeline with NiFi and Power BI

## Overview
This project aims to build a robust data pipeline using Apache NiFi to collect weather data from the OpenWeatherMap API and then analyze it using Power BI. The pipeline operates in batch mode as weather data doesn't require real-time processing.

## Components
1. **Apache NiFi**: A powerful data processing tool used for ingesting, transferring, and processing large volumes of data. NiFi will be responsible for fetching weather data from the OpenWeatherMap API.

2. **OpenWeatherMap API**: An API service providing access to weather data globally. We'll utilize this API to gather weather information for our analysis.

3. **Power BI**: A business analytics tool by Microsoft used for analyzing and visualizing data. Power BI will be employed to analyze the collected weather data and derive insights from it.

## Pipeline Workflow
1. **Data Collection with NiFi**:
   - Apache NiFi will fetch weather data from the OpenWeatherMap API at regular intervals (daily).
   - The NiFi flow will include processors to make HTTP requests to the API, retrieve weather data in JSON format, and store it in a suitable data format (eCSV).

2. **Data Transformation and Storage**:
   - NiFi may perform any necessary data transformations  before storing the data: in this project, a date column is added to the collected data.
   - A python file to run,specifies the details needed to store the data in the CSV file:  CSV file name, columns and port number matching the port number in the  last processor of the Nifi pipeline
   - The transformed data will be stored in a location accessible to Power BI (local CSV file).

3. **Data Analysis with Power BI**:
   - Power BI will connect to the CSV file where the data is stored.
   - Various visualizations, dashboards, and reports will be created in Power BI to analyze and visualize the weather trends.

## Configuration
- **NiFi Configuration**: Set up NiFi to fetch data from the OpenWeatherMap API. Configure the appropriate processors to handle HTTP requests, data transformation, and storage.

- **API Key**: Obtain an API key from OpenWeatherMap to access their API.

- **Power BI Connection**: Configure Power BI to connect to the data source where NiFi stores the weather data.

## Usage
1. Start the NiFi data pipeline.
2. NiFi will automatically fetch weather data from the OpenWeatherMap API according to the configured schedule.
3. Power BI users can then access the stored weather data and perform analysis using Power BI Desktop or Power BI Service.

## Considerations
- **API Rate Limits**: Be mindful of the rate limits imposed by the OpenWeatherMap API to avoid exceeding usage quotas.
- **Data Retention**: Decide on a data retention policy based on storage constraints and analysis requirements.
- **Security**: Ensure that sensitive data such as API keys and access credentials are securely managed and stored.
- **Performance**: Optimize the NiFi flow and Power BI reports for performance, especially when dealing with large volumes of data.in this case, there's no need for streaming data and a batch pipeline with one hour interval would be enough.

## Future Enhancements
- **Real-time Streaming**: Explore the possibility of transitioning to real-time processing if the need arises in the future.
- **Advanced Analytics**: Incorporate advanced analytics techniques such as predictive modeling or machine learning to derive deeper insights from the weather data.
- **Automated Alerts**: Implement automated alerting mechanisms to notify stakeholders of significant weather events or anomalies detected in the data.

## Contributors
- [Fatma Ben Dhieb](https://github.com/fabenp)


