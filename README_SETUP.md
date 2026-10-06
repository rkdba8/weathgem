# Immoweb + Gemini free tier + GitHub Actions

## Secrets GitHub à créer

Repository -> Settings -> Secrets and variables -> Actions -> New repository secret

- `GEMINI_API_KEY`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`

Ne mets jamais ces valeurs dans le code ou dans un fichier commité.

## Premier test

1. Commit/push les fichiers sur la branche par défaut.
2. GitHub -> Actions -> "Veille Immoweb + Gemini" -> Run workflow.
3. `NOTIFY_ALL=1` est volontairement activé au début pour comparer les décisions Gemini aux tiennes.
4. Quand les résultats te conviennent, passe `NOTIFY_ALL` à `0`.

## Notes

- Le workflow garde `seen.json` et `gemini_usage.json` dans le dépôt afin que l'état survive aux runners éphémères.
- Un cap local de 450 appels Gemini par jour laisse une marge sous un quota de 500 RPD.
- Un délai de 4,2 secondes entre les appels évite de dépasser 15 RPM.
- Une annonce n'est pas marquée comme vue si le chargement ou l'appel Gemini échoue.

- `DATE_CIBLE` est vide par défaut : aucune annonce n'est éliminée uniquement parce qu'elle est disponible plus tôt.
