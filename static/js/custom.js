document.addEventListener("DOMContentLoaded", function () {
  // Initialize all tables with data-sortable-filterable
  const tables = document.querySelectorAll('table[data-sortable-filterable="true"]');

  tables.forEach(table => {
    initTable(table);
  });
});

function initTable(table) {
  const filterInputs = table.querySelectorAll(".filter-input");
  const clearButtons = table.querySelectorAll(".clear-filter-btn");
  const filterRow = table.querySelector(".filter-row");
  const toggleBtn = table.closest(".container-fluid")?.querySelector(".toggle-filters-btn");

  // Bind input filters
  filterInputs.forEach(input => {
    input.addEventListener("input", () => filterTable(table));
  });

  // Bind individual column clear buttons
  clearButtons.forEach(button => {
    button.addEventListener("click", () => {
      const col = button.dataset.col;
      const input = table.querySelector(`.filter-input[data-col="${col}"]`);
      if (input) input.value = "";
      filterTable(table);
    });
  });

  // Toggle button (optional)
  if (toggleBtn && filterRow) {
    toggleBtn.addEventListener("click", () => {
      filterRow.classList.toggle("d-none");
      toggleBtn.textContent = filterRow.classList.contains("d-none") ? "Show Filters" : "Hide Filters";
    });
  }

  // Run initial styling
  styleStatusCells(table);
  filterTable(table);
}

// Sort function must be globally accessible
window.sortTable = function (colIndex, tableId) {
  const table = document.getElementById(tableId);
  const tbody = table.tBodies[0];
  const rows = Array.from(tbody.rows);

  let sortDirection = table.dataset.sortDir === "asc" ? false : true;
  table.dataset.sortDir = sortDirection ? "asc" : "desc";

  rows.sort((a, b) => {
    let aText = a.cells[colIndex].innerText.trim().toLowerCase();
    let bText = b.cells[colIndex].innerText.trim().toLowerCase();

    if (!isNaN(aText) && !isNaN(bText)) {
      aText = parseFloat(aText);
      bText = parseFloat(bText);
    }

    if (aText < bText) return sortDirection ? -1 : 1;
    if (aText > bText) return sortDirection ? 1 : -1;
    return 0;
  });

  tbody.innerHTML = "";
  rows.forEach(row => tbody.appendChild(row));

  // Clear existing icons
  const allIcons = document.querySelectorAll(".sort-icon");
  allIcons.forEach(icon => icon.textContent = "");

  // Set icon for active header
  const headers = table.querySelectorAll("th");
  const iconSpan = headers[colIndex].querySelector(".sort-icon");
  iconSpan.textContent = sortDirection ? "▲" : "▼";

  styleStatusCells(table);
  filterTable(table);
};

function filterTable(table) {
  const filterInputs = table.querySelectorAll(".filter-input");
  const rows = Array.from(table.tBodies[0].rows);

  rows.forEach(row => {
    let visible = true;

    filterInputs.forEach(input => {
      const col = parseInt(input.dataset.col);
      const filterValue = input.value.trim().toLowerCase();
      const cellValue = row.cells[col].innerText.trim().toLowerCase();

      if (!cellValue.includes(filterValue)) {
        visible = false;
      }
    });

    row.style.display = visible ? "" : "none";
  });

  styleStatusCells(table);
}

function styleStatusCells(table) {
  const rows = table.tBodies[0].rows;
  for (let row of rows) {
    const statusCell = row.cells[2]; // Adjust this index if needed per table
    const statusText = statusCell?.textContent.trim().toLowerCase();

    statusCell?.classList.remove("status-success", "status-failed", "status-processing", "status-scheduled");

    if (statusText === "success") {
      statusCell.classList.add("status-success");
    } else if (statusText === "failed") {
      statusCell.classList.add("status-failed");
    } else if (statusText === "processing") {
      statusCell.classList.add("status-processing");
    } else if (statusText === "scheduled") {
      statusCell.classList.add("status-scheduled");
    }
  }
}

$(document).ready(function () {
  let counts = {};
  
  $('#statusTable .status').each(function () {
      let status = $(this).text().trim();
      counts[status] = (counts[status] || 0) + 1;
  });

  // Display boxes
  const colorMap = {
      'Success': 'status-success',
      'Failed': 'status-failed',
      'Processing': 'status-processing',
      'Scheduled': 'status-scheduled'
  };

  $.each(counts, function (status, count) {
      let boxClass = colorMap[status] || 'status-other';
      $('#statusSummary').append(
          `<div class="status-box ${boxClass}">${status}: ${count}</div>`
      );
  });
});