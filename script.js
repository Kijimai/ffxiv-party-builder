let charAvatar = ""
const callApi = document.getElementById("call-api")
const charSearch = document.getElementById("char-search")
const displayUsers = document.getElementById("display-users")
const avatar = document.getElementById("avatar")
let isLoading = true
// fetch("https://xivapi.com/character/39449464", { mode: "cors" })
//   .then((res) => res.json())
//   .then((charData) => {
//     console.info(charData.Character)
//     charAvatar = charData.Character.Portrait
//   })

callApi.addEventListener("click", displayAvatar)

/* Adding extended=1 gives more info per request */
async function displayAvatar() {
  await fetch("https://xivapi.com/character/2684564?extended=1")
    .then((res) => res.json())
    .then((data) => {
      avatar.src = data.Character.Avatar
      console.log(data.Character)
    })
}

async function listCharacters(character, server = "") {
  if (isLoading) {
    displayUsers.innerHTML = `
      <div>
        <h2>Loading!!!!</h2>
      </div>
    `
  }
  if (!server) {
    characters = await fetch(
      `https://xivapi.com/character/search?name=${character}&extended=1`
    )
      .then((res) => {
        return res.json()
      })
      .then((data) => {
        // console.info(data.Results)
        console.log(data)
        console.log(data.Results)
        renderCharacters(data.Results)
      })
      .catch((err) => {
        console.log(err)
      })
  } else {
    characters = await fetch(
      `https://xivapi.com/character/search?name=${character}&server=${server}`
    )
      .then((res) => {
        return res.json()
      })
      .then((data) => {
        console.log(data.Results)
        renderCharacters(data.Results)
      })
      .catch((err) => {
        console.log(err)
      })
  }
  isLoading = false
}

function displayLoadingTxt() {
  let loadingText = `<div>
  <h2>LOADING!!!!</h2>
</div>`
  displayUsers.innerHTML = loadingText
}

function renderCharacters(list) {
  let output = ""
  list.map((character) => {
    output += `
      <div key='${character.ID}'>
        <img src=${character.Avatar} alt=${character.Name} />
        <h2>${character.Name}</h2>
      </div>
    `
  })
  displayUsers.innerHTML = output
}

charSearch.addEventListener("submit", (e) => {
  e.preventDefault()
  charName = e.currentTarget.elements.char_name.value
  charServer = e.currentTarget.elements.server_name.value
  listCharacters(charName, charServer)
})

/* 
  Avatar
  Name
  Server
  ID


*/
