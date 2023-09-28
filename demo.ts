import * as fs from 'fs/promises';
import * as path from 'path';

// Simulating Pokémon information
interface PokemonInfo {
  name: string;
  type: string;
  description: string;
}

async (params:type) => {

}          

async (params:type) => {

}

// Simulating a Pokémon Pokédex entry
async function readPokedexEntry() {
  const pokemonName = 'Pikachu';
  const filePath = path.join(__dirname, `${pokemonName.toLowerCase()}.json`);

  try {
    const fileContent = await fs.readFile(filePath, 'utf8');
    const pokemonData: PokemonInfo = JSON.parse(fileContent);

    console.log(`Pokédex entry for ${pokemonData.name}:`);
    console.log(`Type: ${pokemonData.type}`);
    console.log(`Description: ${pokemonData.description}`);
  } catch (err) {
    console.error(`Error reading ${pokemonName}'s Pokédex entry:`, err);
  }
}

readPokedexEntry();
