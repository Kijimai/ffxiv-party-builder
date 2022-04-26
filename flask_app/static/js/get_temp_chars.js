let isLoading = false

async function getTempChars() {
  isLoading = true
  await fetch("https://xivapi.com/character/search?name=Kawaii")
    .then((res) => res.json())
    .then((data) => {
      console.log(data.Results)
      renderFullParty(data.Results)
      renderLightParty(data.Results)
    })
    .catch((err) => {
      console.log(err)
    })
  isLoading = false
}

getTempChars()

function renderFullParty(list) {
  let output = ""
  const fullPartyContainer = document.getElementById("full-party")

  if (isLoading) {
    fullPartyContainer.innerHTML = `<h1>LOADING</h1>`
  }

  for (let i = 0; i < 8; i++) {
    output += `
    <article class="full-party__member-container">
      <img class="full-party__avatar" src="${list[i].Avatar}" alt="${list[i].Name}" />
      <div class="full-party__member-container-inner flex">
        <h3 class="full-party__member-name">${list[i].Name}</h3>
        <div class="full-party__link-container">
          <a class="party-link" href="#">View Character</a>
          <a class="party-link" href="#">Change Character</a>
          <a class="party-link" href="#">Remove From Party</a>
        </div>
      </div>
    </article>
    `
  }
  fullPartyContainer.innerHTML = output
}

function renderLightParty(list) {
  let output = ""
  const lightPartyContainer = document.getElementById("light-party")

  if (isLoading) {
    lightPartyContainer.innerHTML = `<h1>LOADING</h1>`
  }

  for (let i = 0; i < 4; i++) {
    output += `
    <article class="light-party__member-container flex">
      <img class="light-party__avatar" src="${list[i].Avatar}" alt="${list[i].Name}" />
      <div class="light-party__member-container-inner flex">
        <h3 class="light-party__member-name">${list[i].Name}</h3>
        <div class="light-party__link-container flex">
          <a class="party-link" href="#">View Character</a>
          <a class="party-link" href="#">Change Character</a>
          <a class="party-link" href="#">Remove From Party</a>
        </div>
      </div>
    </article>
    `
  }
  lightPartyContainer.innerHTML = output
}
