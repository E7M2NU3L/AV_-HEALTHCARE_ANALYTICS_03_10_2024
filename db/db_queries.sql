show databases;
use av_healthcare_databasee;

show tables;

CREATE TABLE Patient (
    patientid INT AUTO_INCREMENT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    age INT,
    city_code INT
);

create table Hospital (
	case_id INT AUTO_INCREMENT PRIMARY KEY,
	Hospital_code INT NOT NULL,
    Hospital_type_code VARCHAR(2) NOT NULL,
    City_Code_Hospital INT NOT NULL,
    Hospital_region_code VARCHAR(2) NOT NULL,
    Available_Extra_Rooms_in_Hospital INT,
    Department VARCHAR(50) NOT NULL,
    Ward_Type VARCHAR(2) NOT NULL,
    Bed_Grade INT,
    patientid INT,
    City_Code_Patient INT,
    Type_of_Admission VARCHAR(50),
    Severity_of_Illness VARCHAR(50),
    Visitors_with_Patient INT,
    Age VARCHAR(50),
    Admission_Deposit FLOAT,
    Stay VARCHAR(50),
    FOREIGN KEY (patientid) REFERENCES Patient(patientid) ON DELETE CASCADE
);

INSERT INTO Patient (patient_name, gender, age, city_code) VALUES
('Harivansh BR', 'Male', 56, 7),
('RanjithKumar', 'Male', 75, 8),
('Anbu Arasan', 'Male', 45, 3),
('Divya Priya', 'Female', 36, 5),
('Karthikeyan M', 'Male', 25, 6),
('Meenakshi S', 'Female', 65, 4),
('Venkatesh R', 'Male', 58, 9),
('Saravanan K', 'Male', 72, 2),
('Priya Dharshini', 'Female', 33, 10),
('Gokulnath S', 'Male', 27, 1),
('Sundaravel P', 'Male', 54, 7),
('Lakshmi Narayanan', 'Male', 62, 8),
('Swathi R', 'Female', 42, 5),
('Muthukumar B', 'Male', 37, 3),
('Revathi M', 'Female', 29, 6);

show tables;

select * from patient;

INSERT INTO Hospital (Hospital_code, Hospital_type_code, City_Code_Hospital, Hospital_region_code, 
    Available_Extra_Rooms_in_Hospital, Department, Ward_Type, Bed_Grade, 
    patientid, City_Code_Patient, Type_of_Admission, Severity_of_Illness, Visitors_with_Patient, 
    Age, Admission_Deposit, Stay) 
VALUES
(8, 'c', 3, 'Z', 3, 'radiotherapy', 'R', 2, 1, 7, 'Emergency', 'Extreme', 2, 56, 4911, '0-10'),
(2, 'c', 5, 'Z', 2, 'radiotherapy', 'S', 2, 1, 7, 'Trauma', 'Extreme', 2, 56, 5954, '41-50'),
(10, 'e', 1, 'X', 2, 'anesthesia', 'S', 2, 1, 7, 'Trauma', 'Extreme', 2, 56, 4745, '31-40'),
(26, 'b', 2, 'Y', 2, 'radiotherapy', 'R', 2, 2, 8, 'Trauma', 'Extreme', 2, 75, 7272, '41-50'),
(26, 'b', 2, 'Y', 2, 'radiotherapy', 'S', 2, 2, 8, 'Trauma', 'Extreme', 2, 75, 5558, '41-50'),
(23, 'a', 6, 'X', 2, 'anesthesia', 'S', 2, 3, 3, 'Trauma', 'Extreme', 2, 45, 4449, 'Nov-20'),
(32, 'f', 9, 'Y', 1, 'radiotherapy', 'S', 3, 3, 3, 'Emergency', 'Extreme', 2, 45, 6167, '0-10'),
(23, 'a', 6, 'X', 4, 'radiotherapy', 'Q', 3, 4, 5, 'Trauma', 'Extreme', 2, 36, 5571, '41-50'),
(1, 'd', 10, 'Y', 2, 'gynecology', 'R', 4, 4, 5, 'Trauma', 'Extreme', 2, 36, 7223, '51-60'),
(10, 'e', 1, 'X', 2, 'gynecology', 'S', 3, 5, 6, 'Trauma', 'Extreme', 2, 25, 6056, '31-40'),
(22, 'g', 9, 'Y', 2, 'radiotherapy', 'S', 2, 6, 4, 'Urgent', 'Extreme', 2, 65, 5797, '21-30'),
(26, 'b', 2, 'Y', 4, 'radiotherapy', 'R', 1, 7, 9, 'Urgent', 'Extreme', 2, 58, 5993, 'Nov-20'),
(16, 'c', 3, 'Z', 2, 'radiotherapy', 'R', 3, 8, 2, 'Emergency', 'Extreme', 2, 72, 5141, '0-10'),
(9, 'd', 5, 'Z', 3, 'radiotherapy', 'S', 3, 9, 10, 'Urgent', 'Extreme', 2, 33, 8477, '21-30'),
(6, 'a', 6, 'X', 4, 'gynecology', 'Q', 3, 10, 1, 'Emergency', 'Extreme', 2, 27, 2685, '0-10'),
(6, 'a', 6, 'X', 3, 'gynecology', 'Q', 3, 11, 7, 'Emergency', 'Extreme', 2, 54, 9398, '0-10'),
(23, 'a', 6, 'X', 4, 'radiotherapy', 'Q', 3, 12, 8, 'Urgent', 'Extreme', 4, 62, 2933, '0-10'),
(29, 'a', 4, 'X', 4, 'anesthesia', 'S', 3, 13, 5, 'Emergency', 'Extreme', 2, 42, 5342, 'Nov-20'),
(32, 'f', 9, 'Y', 4, 'radiotherapy', 'S', 2, 14, 3, 'Trauma', 'Extreme', 2, 37, 7442, '21-30'),
(12, 'a', 9, 'Y', 4, 'radiotherapy', 'Q', 2, 15, 6, 'Trauma', 'Extreme', 2, 29, 5155, '31-40');

select * from hospital;

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
    
SELECT 
    h.Severity_of_Illness,
    COUNT(h.case_id) AS Total_Cases
FROM 
    Hospital h
GROUP BY 
    h.Severity_of_Illness
ORDER BY 
    Total_Cases DESC;

SELECT 
    h.Type_of_Admission,
    COUNT(h.case_id) AS Total_Admissions
FROM 
    Hospital h
GROUP BY 
    h.Type_of_Admission
ORDER BY 
    Total_Admissions DESC;
    
SELECT 
    h.City_Code_Patient,
    COUNT(h.patientid) AS Total_Patients
FROM 
    Hospital h
GROUP BY 
    h.City_Code_Patient
ORDER BY 
    Total_Patients DESC;
    
SELECT 
    h.Age,
    COUNT(h.patientid) AS Total_Patients
FROM 
    Hospital h
GROUP BY 
    h.Age
ORDER BY 
    Total_Patients DESC;
    
SELECT 
    h.Stay,
    COUNT(h.case_id) AS Total_Patients
FROM 
    Hospital h
GROUP BY 
    h.Stay
ORDER BY 
    Total_Patients DESC;



