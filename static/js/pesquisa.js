// Adicione o seguinte código ao seu arquivo JavaScript

const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const searchButton = document.getElementById('search-button');
const searchResults = document.getElementById('search-results');

searchButton.addEventListener('click', (e) => {
  e.preventDefault();
  const searchTerm = searchInput.value.trim();
  if (searchTerm) {
    fetch('/search', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ searchTerm })
    })
   .then(response => response.json())
   .then(data => {
      const results = data.results;
      searchResults.innerHTML = '';
      results.forEach((result) => {
        const resultHTML = `
          <li>
            <a href="${result.url}">${result.title}</a>
          </li>
        `;
        searchResults.innerHTML += resultHTML;
      });
      searchResults.style.display = 'block';
    })
   .catch(error => console.error(error));
  }
});

searchInput.addEventListener('keyup', (e) => {
  if (e.key === 'Enter') {
    searchButton.click();
  }
});

