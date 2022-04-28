const searchCharactersForm = document.getElementById("search-characters")

searchCharactersForm.addEventListener("submit", (e) => {
  e.preventDefault()
  const characterName = e.target[0].value
  const serverName = e.target[1].value
  console.log(e)
  console.log(characterName, serverName)
  searchCharacters(characterName, serverName)
})

async function searchCharacters(characterName, serverName = "") {
  isLoading = true
  // if (isLoading) {
  //   displayUsers.innerHTML = `
  //     <div>
  //       <h2>Loading!!!!</h2>
  //     </div>
  //   `
  // }
  if (!serverName) {
    characters = await fetch(
      `https://xivapi.com/character/search?name=${characterName}&extended=1`
    )
      .then((res) => {
        return res.json()
      })
      .then((data) => {
        // console.info(data.Results)
        console.log(data)
        console.log(data.Results)
        renderResults(data.Results)
      })
      .catch((err) => {
        console.log(err)
      })
  } else {
    characters = await fetch(
      `https://xivapi.com/character/search?name=${characterName}&server=${serverName}`
    )
      .then((res) => {
        return res.json()
      })
      .then((data) => {
        console.log(data)
        console.log(data.Results)
        renderResults(data.Results)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  isLoading = false
}

// TODO: Pagination
// async function changePage() {

// }

function renderResults(list) {
  let output = ""
  const searchResults = document.getElementById("search_results_container")
  list.map((character) => {
    console.log(character)
    output += `
    <article>
      <img src=${character.Avatar} alt=${character.Name} />
      <form>
      <p>${character.Name}</p>
        <a href="/characters/${character.ID}">View Character</a>
      </form>
    </article>
    `
  })
  searchResults.innerHTML = output
}

//Trouble sending specific ID from API call to Flask, to later render in Jinja by using that same ID to call the API using Jinja
