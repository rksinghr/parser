//----------------------------Sort Table----------------------------------------------//
document.addEventListener('DOMContentLoaded', function () {
  let sortDirection = true;
  let lastSortedCol = null;
  styleStatusCells(); // call on load

  window.sortTable = function(colIndex) {
    const table = document.getElementById("statusLogTable");
    const tbody = table.tBodies[0];
    const rows = Array.from(tbody.rows);

    rows.sort((a, b) => {
      let aText = a.cells[colIndex].innerText.trim();
      let bText = b.cells[colIndex].innerText.trim();

      let aVal = isNaN(aText) ? aText.toLowerCase() : parseFloat(aText);
      let bVal = isNaN(bText) ? bText.toLowerCase() : parseFloat(bText);

      if (aVal < bVal) return sortDirection ? -1 : 1;
      if (aVal > bVal) return sortDirection ? 1 : -1;
      return 0;
    });

      // Update sort direction
    if (lastSortedCol === colIndex) {
      sortDirection = !sortDirection;
    } else {
      sortDirection = true; // reset to ascending if new column
    }
    lastSortedCol = colIndex;

    // sortDirection = !sortDirection;
    tbody.innerHTML = "";
    rows.forEach(row => tbody.appendChild(row));
    styleStatusCells();

    // Clear existing icons
    const allIcons = document.querySelectorAll(".sort-icon");
    allIcons.forEach(icon => icon.textContent = "");

    // Set icon for active header
    const headers = table.querySelectorAll("th");
    const iconSpan = headers[colIndex].querySelector(".sort-icon");
    iconSpan.textContent = sortDirection ? "▲" : "▼";

  };
});
//-----------------------------Filter Table---------------------------------------------//
document.addEventListener("DOMContentLoaded", function () {
  const filterInputs = document.querySelectorAll(".filter-input");
  const clearButtons = document.querySelectorAll(".clear-filter-btn");
  styleStatusCells(); // call on load
  // Bind input filtering
  filterInputs.forEach(input => {
    input.addEventListener("input", filterTable);
  });

  // Bind individual clear buttons
  clearButtons.forEach(button => {
    button.addEventListener("click", function () {
      const colIndex = button.dataset.col;
      const input = document.querySelector(`.filter-input[data-col="${colIndex}"]`);
      if (input) {
        input.value = "";
        filterTable();
      }
    });
  });

  function filterTable() {
    const table = document.getElementById("statusLogTable");
    const tbody = table.tBodies[0];
    const rows = Array.from(tbody.rows);

    rows.forEach(row => {
      let visible = true;

      filterInputs.forEach(input => {
        const colIndex = parseInt(input.dataset.col);
        const filterValue = input.value.toLowerCase();
        const cellValue = row.cells[colIndex].innerText.toLowerCase();

        if (!cellValue.includes(filterValue)) {
          visible = false;
        }
      });

      row.style.display = visible ? "" : "none";
      styleStatusCells();
    });
  }
});
//-------------------------------Style Status Cell-------------------------------------------//
function styleStatusCells() {
  const table = document.getElementById("statusLogTable");
  const rows = table.tBodies[0].rows;

  for (let row of rows) {
    const statusCell = row.cells[2]; // Status column index
    const statusText = statusCell.textContent.trim().toLowerCase();

    // Remove old classes (optional)
    statusCell.classList.remove("status-success", "status-failed");

    // Add new based on value
    if (statusText === "success") {
      statusCell.classList.add("status-success");
    } else if (statusText === "failed") {
      statusCell.classList.add("status-failed");
    }
  }
}
