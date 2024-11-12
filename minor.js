function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}

// Function to convert FormData to JSON
function formDataToJson(formData) {
    const obj = {};
    formData.forEach((value, key) => {
        obj[key] = value;
    });
    return obj;
}

// Handle Add Patient form submission
document.getElementById('addPatientForm').onsubmit = function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const jsonData = JSON.stringify(formDataToJson(formData));
    
    fetch('/add_patient/', {
        method: 'POST',
        body: jsonData,
        headers: { 
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        }
    }).then(response => response.json()).then(data => {
        alert(data.message || 'Patient added successfully');
        closeModal('addPatientModal');
    }).catch(error => {
        console.error('Error:', error);
        alert('Something went wrong!');
    });
};

// Handle Add Donor form submission
document.getElementById('addDonorForm').onsubmit = function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const jsonData = JSON.stringify(formDataToJson(formData));
    
    fetch('/add_donor/', {
        method: 'POST',
        body: jsonData,
        headers: { 
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        }
    }).then(response => response.json()).then(data => {
        alert(data.message || 'Donor added successfully');
        closeModal('addDonorModal');
    }).catch(error => {
        console.error('Error:', error);
        alert('Something went wrong!');
    });
};

// Handle Predict Compatibility form submission
document.getElementById('predictForm').onsubmit = function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const jsonData = JSON.stringify(formDataToJson(formData));
    
    fetch('/predict_compatibility/', {
        method: 'POST',
        body: jsonData,
        headers: { 
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
        }
    }).then(response => response.json()).then(data => {
        if (data.success) {
            alert('Compatible');
        } else {
            alert('Not compatible');
        }
        closeModal('predictModal');
    }).catch(error => {
        console.error('Error:', error);
        alert('Something went wrong!');
    });
};

// Simple function to close modal (make sure it's defined in your project)
function closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = 'none'; // or any other modal hiding logic you have
    }
}

