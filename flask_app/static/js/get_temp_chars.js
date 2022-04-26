let isLoading = false

async function getTempChars() {
  isLoading = true
  await fetch("https://xivapi.com/character/search?name=Kawaii")
    .then((res) => res.json())
    .then((data) => {
      console.log(data.Results)
      renderParty(data.Results)
    })
    .catch((err) => {
      console.log(err)
    })
  isLoading = false
}

getTempChars()

function renderParty(list) {
  let output = ""
  const fullPartyContainer = document.getElementById("full-party")

  if (isLoading) {
    fullPartyContainer.innerHTML = `<h1>LOADING</h1>`
  }

  for (let i = 0; i < 8; i++) {
    output += `
    <article class="full-party__member-container">
      <img class="full-party__avatar" src="${list[i].Avatar} alt="${list[i].Name}" />
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
