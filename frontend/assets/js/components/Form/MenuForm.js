import { $, createElement } from "../utils/dom.js";

// Resets the input form to its default state for creating a new menu
export function resetForm() {
  // Use the native .reset() method on the HTML form element
  $("menuForm").reset();

  // Change the submit button text back to "Add menu"
  $("submitBtn").textContent = "Add Menu";

  // Hide the "Cancel" button, as we are no longer in 'edit' mode
  $("cancelBtn").style.display = "none";
}

// Populates the input form fields with data from a selected menu object (for editing)
export function fillForm(menu) {
  // Fill each input field with the corresponding property from the menu data
  $("Category").value = menu.Category;
  $("Name").value = menu.Name;
  $("Price").value = menu.Price;
  $("rating").value = menu.rating;

  // Change the submit button text to "Update menu"
  $("submitBtn").textContent = "Update Menu";

  // Show the "Cancel" button, allowing the user to exit 'edit' mode
  $("cancelBtn").style.display = "inline-block";
}