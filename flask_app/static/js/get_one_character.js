async function displayAvatar() {
  await fetch("https://xivapi.com/character/9426169?extended=1")
    .then((res) => res.json())
    .then((data) => {
      console.log(data.Character)
      renderOneCharacter(data.Character)
    })
    .catch((err) => console.log(err))
}

function renderOneCharacter(charInfo) {
  const {
    Portrait,
    Avatar,
    Bio,
    ID,
    Name: CharName,
    NameDay,
    Server,
    FreeCompanyName,
    Race: { Name: RaceName },
    GearSet: {
      Job: { Name: JobName, Abbreviation: JobAbbreviation, Icon: JobIcon },
      Class: { Name: ClassName, ClassAbbreviation, Icon: ClassIcon },
    },
    GrandCompany: {
      Company: { Name: GCName },
    },
    Title: { Name: PlayerTitle },
    DC: DataCenter,
  } = charInfo
  let output = ""
  const singleChar = document.getElementById("show-one-char")

  output += `
  <article class="single-character flex">
    <div class="single-character__photo-container">
      <img class="single-character__image" src=${Portrait} alt=${CharName} />
    </div>
    <div class="single-character__info-container">
      <h2>${CharName}</h2>
      <table>
        <tr>
          <th>Race:</th>
          <td>${RaceName}</td>
        </tr>
        <tr>
          <th>Title:</th>
          <td>${PlayerTitle}</td>
        </tr>
        <tr>
          <th>Bio:</th>
          <td>${Bio}</td>
        </tr>
        <tr>
          <th>Job Class:</th>
          <td>${ClassName}<img class="job-icon" src="https://xivapi.com/${ClassIcon}" alt="${ClassName}"/></td>
          <td>/</td>
          <td>${JobName}<img class="job-icon" src="https://xivapi.com/${JobIcon}" alt="${JobName}"/></td>
        </tr>
        <tr>
          <th>Free Company: </th>
          <td>${FreeCompanyName}</td>
        </tr>
        <tr>
          <th>Grand Company: </th>
          <td>${GCName}</td>
        </tr>
        <tr>
          <th>Data Center:</th>
          <td>${DataCenter}</td>
        </tr>
        <tr>
          <th>Server Name:</th>
          <td>${Server}</td>
        </tr>
      </table>
      <form class="" action="/" method="POST">
        <input type="hidden" value="${CharName}" name="character_name" />
        <input type="hidden" value="${RaceName}" name="character_race" />
        <input type="hidden" value="${PlayerTitle}" name="character_title" />
        <input type="hidden" value="${Bio}" name="character_bio" />
        <input type="hidden" value="${JobName}" name="character_job" />
        <input type="hidden" value="${ClassName}" name="character_class" />
        <input type="hidden" value="${FreeCompanyName}" name="character_free_company" />
        <input type="hidden" value="${GCName}" name="character_grand_company" />
        <input type="hidden" value="${DataCenter}" name="character_data_center" />
        <input type="hidden" value="${Server}" name="character_server" />
        <input type="hidden" value="${Portrait}" name="character_portrait_url" />
        <input type="hidden" value="${Avatar}" name="character_avatar_url" />
        <button>Add To Light Party</button>
      </form>
    </div>
  </article>
  `
  singleChar.innerHTML = output
}

displayAvatar()
