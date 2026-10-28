import { pistol } from "./pistol.js";
import { rifle } from "./rifle.js";
import { rimfire } from "./rimfire.js";
import { shotshell } from "./shotshell.js";
import type { Round } from "./types.js";

export type { Cartridge, Shotshell, Round } from "./types.js";
export { pistol, rifle, rimfire, shotshell };

export const all: readonly Round[] = [...rifle, ...pistol, ...rimfire, ...shotshell];

const key = (s: string) => s.toLowerCase().replace(/[\s.\-_"']+/g, "");
const index = new Map<string, Round>();
for (const round of all) {
  // Earlier sets win on clashes, so "44 Rem Mag" resolves to one record; use find() with
  // a category to pick the other.
  for (const name of [round.name, ...("aliases" in round ? round.aliases : [])]) {
    if (!index.has(key(name))) index.set(key(name), round);
  }
}

/**
 * Look up a cartridge or shotshell by name or alias, ignoring case, spaces and punctuation.
 * `"308 win"`, `"308 Winchester"` and `".308WIN"` all match.
 */
export function find(name: string, category?: Round["category"]): Round | undefined {
  if (category) {
    return all.find((r) => r.category === category &&
      [r.name, ...("aliases" in r ? r.aliases : [])].some((n) => key(n) === key(name)));
  }
  return index.get(key(name));
}
