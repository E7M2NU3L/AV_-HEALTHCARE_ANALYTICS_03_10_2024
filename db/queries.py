class DBQueries:
    def __init__(self) -> None:
        pass

    def fetcg_patient_details(self) -> str:
        return """
            SELECT 
                p.patientid,
                p.patient_name,
                p.gender,
                p.age,
                p.city_code AS Patient_City_Code,
                h.case_id,
                h.Hospital_code,
                h.Department,
                h.Ward_Type,
                h.Bed_Grade,
                h.Type_of_Admission,
                h.Severity_of_Illness,
                h.Visitors_with_Patient,
                h.Age AS Age_Group,
                h.Admission_Deposit,
                h.Stay
            FROM 
                Patient p
            JOIN 
                Hospital h ON p.patientid = h.patientid
            ORDER BY 
                h.case_id;
            """
    
    def bed_utilization_report(self) -> str:
        return """
            SELECT 
                h.Hospital_code,
                COUNT(h.case_id) AS Total_Patients_Admitted,
                SUM(h.Available_Extra_Rooms_in_Hospital) AS Extra_Rooms_Available
            FROM 
                Hospital h
            GROUP BY 
                h.Hospital_code
            ORDER BY 
                Total_Patients_Admitted DESC;

            """
    
    def severity_analysis(self) -> str:
        return """
            SELECT 
                h.Severity_of_Illness,
                COUNT(h.case_id) AS Total_Cases
            FROM 
                Hospital h
            GROUP BY 
                h.Severity_of_Illness
            ORDER BY 
                Total_Cases DESC;

            """
    
    def admission_type_details(self) -> str:
        return """
            SELECT 
                h.Type_of_Admission,
                COUNT(h.case_id) AS Total_Admissions
            FROM 
                Hospital h
            GROUP BY 
                h.Type_of_Admission
            ORDER BY 
                Total_Admissions DESC;
            """
    
    def city_wise_patients(self) -> str:
        return """
        SELECT 
            h.City_Code_Patient,
            COUNT(h.patientid) AS Total_Patients
        FROM 
            Hospital h
        GROUP BY 
            h.City_Code_Patient
        ORDER BY 
            Total_Patients DESC;
        """

    def patient_age_group(self) -> str:
        return """
            SELECT 
                h.Age,
                COUNT(h.patientid) AS Total_Patients
            FROM 
                Hospital h
            GROUP BY 
                h.Age
            ORDER BY 
                Total_Patients DESC;
            """
    
    def stay_duration_analysis(self) -> str:
        return """
            SELECT 
                h.Stay,
                COUNT(h.case_id) AS Total_Patients
            FROM 
                Hospital h
            GROUP BY 
                h.Stay
            ORDER BY 
                Total_Patients DESC;
        """
    
    def hospital_department_statistics(self) -> str:
        return """
            SELECT 
                h.Department,
                COUNT(h.case_id) AS Total_Cases
            FROM 
                Hospital h
            GROUP BY 
                h.Department
            ORDER BY 
                Total_Cases DESC;
            """