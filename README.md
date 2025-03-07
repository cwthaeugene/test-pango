1. **Test Case: Verify `get_current_weather` with Celsius Metric and English Language**

   - Validate Status Code.
   - Insert temperature and feels_like responses for each city into the database.
   - Verify that temperature and feels_like from the database are equal to the API response.

2. **Test Case: Utilize Weather Data for Multiple Cities via City ID Parameter**

   Example API Endpoint: `https://api.openweathermap.org/data/2.5/weather?id={city id}&appid={API key}`

   - Insert temperature and feels_like responses for each city into the database.
   - Create a new database column for the average temperature of each city.
   - Assert that the data inserted into the database is equal to the API response.
   - Print the city with the highest average temperature.

3. **Enhancement: Dynamic API Key and Base URL Configuration**

   - Implement the ability to retrieve the API KEY and BASE URL from `config.ini` for API calls.

4. **Web Question: City Temperature Discrepancy Analysis**

   - Execute a comparative temperature analysis for a minimum of 100 cities using data from both (https://www.timeanddate.com/weather/) and the [OpenWeatherMap API]   
   Example API Endpoint: `https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}`.
   
   - Identify a relevant API to acquire city names for testing.
   
   - Employ Selenium to extract temperature data from the specified website.
   
   - Ensure continuity by utilizing the same database from previous questions.

   Upon completion, generate a concise report highlighting cities with temperature differences between data obtained from the website and the OpenWeatherMap API.


**API Documentation:** [OpenWeatherMap Current Weather API](https://openweathermap.org/current)

**Installation:**
- Run either `pip install -r requirements.txt` or individually install required packages with `pip install requests pytest`.
