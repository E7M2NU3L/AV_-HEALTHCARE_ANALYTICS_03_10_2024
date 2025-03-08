import streamlit as st

test_input_columns = ['Hospital_code', 'Hospital_type_code', 'City_Code_Hospital',
       'Hospital_region_code', 'Available Extra Rooms in Hospital',
       'Department', 'Ward_Type', 'Ward_Facility_Code', 'City_Code_Patient', 'Type of Admission',
       'Bed Grade', 'Visitors with Patient', 'Age',
       'Admission_Deposit']

st.title("AV Healthcare Analysis - Feb 2025")
st.write("Patient Severity Predictor Model")

with st.form(key="patient_analyser"):
    inputs = []
    for columns in test_input_columns:
        value = st.number_input(columns)
        inputs.append(value)

    submit_button = st.form_submit_button(label="Predict")

st.title("Reports Made for the Month")

st.markdown("# Power BI Reports")
st.markdown("hospital and patient's data were analyzed with respect to various metrics")

st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc26720034090f4869/view?project=67bc42e500120c3b7c09")

st.markdown("# Python Reports & Analytics")
st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc3844002ef606bb4d/view?project=67bc42e500120c3b7c09")
st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc383d0022fdf0f103/view?project=67bc42e500120c3b7c09")
st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc3837000705898474/view?project=67bc42e500120c3b7c09")
st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc384c00157a791f0d/view?project=67bc42e500120c3b7c09")

st.title("A Complete MLOps Functionalty with MLFlow")

st.markdown("# MLFLow Pipelines and Logging of metrics.")
st.markdown("an ensemble model is made with random forest bagging model, with decision tree classifier connected to the adaboost boosting model and for the final model gaussian naive bayes model is used.")
st.markdown("All the three models are connected in a voting classifier with soft margin")

st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc3666002b73d02dc9/view?project=67bc42e500120c3b7c09")

st.markdown("# Metrics and MetaData of the model uploaded in the MLFlow pipeline")
st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc365f003375214e0c/view?project=67bc42e500120c3b7c09")
st.image("https://cloud.appwrite.io/v1/storage/buckets/67bc4318002f0fb618ba/files/67cc3657001ea03a840f/view?project=67bc42e500120c3b7c09")


st.markdown("# Model Parameters")
st.markdown("""
        {'estimators': [
            ('rf', RandomForestClassifier(criterion='entropy', max_depth=12, n_estimators=50)), 
            
            ('ad', AdaBoostClassifier(
                estimator=DecisionTreeClassifier(max_features='sqrt',min_weight_fraction_leaf=0,                         
                random_state=42),
            random_state=42)),
             
            ('gn', GaussianNB())], 
            
            'flatten_transform': True, 'n_jobs': None, 'verbose': False, 'voting': 'soft', 
            'weights': None, 
            
            'rf': RandomForestClassifier(criterion='entropy', max_depth=12, n_estimators=50), 
            
            'ad': AdaBoostClassifier(estimator=DecisionTreeClassifier(max_features='sqrt',
                   min_weight_fraction_leaf=0, random_state=42),
                   random_state=42), 
            
            'gn': GaussianNB(), 
            
            'rf__bootstrap': True, 'rf__ccp_alpha': 0.0, 'rf__class_weight': None, 
            
            'rf__criterion': 'entropy', 'rf__max_depth': 12, 'rf__max_features': 'sqrt', 
            
            'rf__max_leaf_nodes': None, 'rf__max_samples': None, 
            
            'rf__min_impurity_decrease': 0.0, 'rf__min_samples_leaf': 1, 
            
            'rf__min_samples_split': 2, 'rf__min_weight_fraction_leaf': 0.0, 
            
            'rf__monotonic_cst': None, 'rf__n_estimators': 50, 'rf__n_jobs': None, 
            
            'rf__oob_score': False, 'rf__random_state': None, 'rf__verbose': 0, 
            
            'rf__warm_start': False, 'ad__algorithm': 'SAMME.R', 
            
            'ad__estimator__ccp_alpha': 0.0, 'ad__estimator__class_weight': None, 
            
            'ad__estimator__criterion': 'gini', 'ad__estimator__max_depth': None, 
            
            'ad__estimator__max_features': 'sqrt', 'ad__estimator__max_leaf_nodes': None, 
            
            'ad__estimator__min_impurity_decrease': 0.0, 'ad__estimator__min_samples_leaf': 1,
             'ad__estimator__min_samples_split': 2, 
            
            'ad__estimator__min_weight_fraction_leaf': 0, 'ad__estimator__monotonic_cst': None,
             'ad__estimator__random_state': 42, 'ad__estimator__splitter': 'best', 
            
            'ad__estimator': DecisionTreeClassifier(max_features='sqrt', 
            
            min_weight_fraction_leaf=0, random_state=42), 
            
            'ad__learning_rate': 1.0, 'ad__n_estimators': 50, 'ad__random_state': 42,
             'gn__priors': None, 'gn__var_smoothing': 1e-09}
         """)

st.markdown("# Model Training")
st.markdown("""
    # Bagging Model
rf = RandomForestClassifier(
    n_estimators=50,
    criterion="entropy",
    max_depth=12
)

# Boosting Model
dt = DecisionTreeClassifier(
    criterion = "gini",
    splitter = "best",
    max_depth= None,
    min_samples_split= 2,
    min_samples_leaf = 1,
    min_weight_fraction_leaf = 0,
    max_features = 'sqrt',
    random_state = 42
)
ad = AdaBoostClassifier(dt, n_estimators=50, learning_rate=1.0, random_state=42)

# Probabilistic Model
gnb = GaussianNB()

# Voting Model
main_model = VotingClassifier([
    ("rf", rf),
    ("ad", ad),
    ("gn", gnb)
], voting="hard")
""")