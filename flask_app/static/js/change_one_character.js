const changeUserForm = document.getElementById("change_user_form")

//Search for characters then change
changeUserForm.addEventListener("submit", (e) => {
  e.preventDefault()
  console.log("submitted!")
  const charName = e.target[0].value
  const serverName = e.target[1].value
  console.log(charName, serverName)
  fetchCharacter(charName, serverName)
})

async function fetchCharacter(characterName, serverName = "") {
  const foundCharacters = await fetch(
    `https://xivapi.com/character/search?name=${characterName}&server=${serverName}`
  )
    .then((res) => res.json())
    .then((data) => {
      return renderCharactersForChange(data.Results)
    })
    .catch((err) => console.log(err))

  console.log(foundCharacters)
}

function renderCharactersForChange(list) {
  let output = ""
  // let isLoading = true
  const searchResults = document.getElementById("search-results")

  // if (isLoading) {
  //   output = `<div>
  //     <h2>Loading...</h2>
  //   </div>`
  //   searchResults.innerHTML = output
  // }

  list.map((foundCharacter) => {
    console.log(foundCharacter)
    output += `
      <article>
        <h2>${foundCharacter.Name}</h2>
        <a target="_blank" rel="noreferrer noopener" href="/characters/${foundCharacter.ID}"><img src="${foundCharacter.Avatar}" alt="${foundCharacter.Name}"/></a>

      </article>
    `
  })
  searchResults.innerHTML = output
}
