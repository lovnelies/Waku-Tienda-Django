const url = "https://dummyjson.com/users";
const answerTable = document.querySelector("#answerTable");

document.addEventListener("DOMContentLoaded", callApi);

function callApi() {
    fetch(url, { mode: 'cors' })
        .then(response => response.json())
        .then(data => showHTML(data))
        .catch(error => console.error('Error fetching data:', error));
}

function showHTML(data) {
    data.users.forEach(element => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td><img src="${element.image}" alt="Avatar" class="img-fluid" width="50" height="50"></td>
            <td>${element.firstName} ${element.lastName}</td>
            <td>${element.domain}</td>
            <td>Mangas ${element.company.name}</td>
        `;
        answerTable.appendChild(row);
    });
}