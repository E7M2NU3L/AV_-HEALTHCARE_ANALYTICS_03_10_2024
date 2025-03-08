import logging
from mysql.connector.cursor import MySQLCursor
from queries import DBQueries

class RunQueries:
    """Class to execute queries on the database."""

    def __init__(self, cursor: MySQLCursor) -> None:
        self.cursor = cursor
        self.db_queries = DBQueries()  # Initialize DBQueries class

    def execute_query(self, query: str):
        """Executes a query and fetches the results."""
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()  # Fetch all results
            return results
        except Exception as e:
            logging.error(f"❌ Error executing query: {e}")
            return None

    def fetch_patient_details(self):
        """Fetch patient details along with hospital information."""
        return self.execute_query(self.db_queries.fetcg_patient_details())

    def bed_utilization(self):
        """Fetch hospital bed utilization report."""
        return self.execute_query(self.db_queries.bed_utilization_report())

    def severity_analysis(self):
        """Fetch severity analysis report."""
        return self.execute_query(self.db_queries.severity_analysis())

    def admission_type_report(self):
        """Fetch admission type report."""
        return self.execute_query(self.db_queries.admission_type_details())

    def city_wise_patient_distribution(self):
        """Fetch city-wise patient distribution."""
        return self.execute_query(self.db_queries.city_wise_patients())

    def patient_age_group_analysis(self):
        """Fetch patient age group distribution."""
        return self.execute_query(self.db_queries.patient_age_group())

    def stay_duration_report(self):
        """Fetch stay duration statistics."""
        return self.execute_query(self.db_queries.stay_duration_analysis())

    def hospital_department_statistics(self):
        """Fetch hospital department statistics."""
        return self.execute_query(self.db_queries.hospital_department_statistics())
