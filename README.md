# FFXIV Party Builder

## What is this?

This app uses the FFXIV API, allowing the user to register and find their character and create a group.

## API Endpoints used

###

```js
"https://xivapi.com/character/${character_ID}&extended=1"
```

### This endpoint gives a more detailed response for a specific character

```js
"https://xivapi.com/character/search?name=${character}&extended=1"
```

## What does it do

- A user can register an account and login.
- On first login, the user will be prompted to search for their character and select their character.
- They can later choose to change their character.
- They will then be allowed to search up other players' characters to compose their 4-person or 8-person party.
  They can choose to have less as well.
- The user can also name and rename their party.
