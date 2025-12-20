import { $, createElement } from "../utils/dom.js";

// Resets the input form to its default state for creating a new staff
export function resetForm() {
  // Use the native .reset() method on the HTML form element
  $("staffForm").reset();

  // Change the submit button text back to "Add staff"
  $("submitBtn").textContent = "Add Staff";

  // Hide the "Cancel" button, as we are no longer in 'edit' mode
  $("cancelBtn").style.display = "none";
}

// Populates the input form fields with data from a selected staff object (for editing)
export function fillForm(staff) {
  // Fill each input field with the corresponding property from the staff data
  $("name").value = staff.name;
  $("email").value = staff.email;
  $("Age").value = staff.Age;

  // Change the submit button text to "Update Student"
  $("submitBtn").textContent = "Update Staff";

  // Show the "Cancel" button, allowing the user to exit 'edit' mode
  $("cancelBtn").style.display = "inline-block";
}