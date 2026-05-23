# Use Apify's Python base image
FROM apify/actor-python:3.12

# Copy the source code
COPY . ./

# Run the test script
CMD ["python", "main.py"]