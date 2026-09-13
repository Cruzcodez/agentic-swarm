#!/usr/bin/env bash
# Installs one or more agents into Kiro.
#
# Kiro reads custom agents from .kiro/agents/ in a project (that project only)
# or ~/.kiro/agents/ (every project). This copies the built Kiro file for each
# agent you name into whichever of those you choose.
#
# Usage:
#   scripts/install-kiro.sh security-reviewer            -> ~/.kiro/agents/  (global)
#   scripts/install-kiro.sh --project security-reviewer  -> ./.kiro/agents/  (this project)
#   scripts/install-kiro.sh --all                        -> every agent, global
set -euo pipefail
cd "$(dirname "$0")/.."

dest="$HOME/.kiro/agents"
agents=()
for arg in "$@"; do
  case "$arg" in
    --project) dest="$PWD/.kiro/agents" ;;
    --all) for d in agents/*/; do agents+=("$(basename "$d")"); done ;;
    *) agents+=("$arg") ;;
  esac
done
[ ${#agents[@]} -gt 0 ] || { echo "name at least one agent, or --all"; exit 1; }

mkdir -p "$dest"
for a in "${agents[@]}"; do
  src="agents/$a/dist/kiro/$a.md"
  [ -f "$src" ] || { echo "no built file for $a. Run scripts/build.sh."; exit 1; }
  cp "$src" "$dest/$a.md"
  echo "installed $a -> $dest/$a.md"
done
echo
echo "In Kiro, switch to an agent by name, or ask the main agent to use it as a sub-agent."
