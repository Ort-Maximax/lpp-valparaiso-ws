# Valparaiso - Service FFMPEG

Ce service est utilisé pour réaliser les actions FFMPEG. 

Il nécessite : 
- [FFMPEG] pour l'utilisation des fonctionnalités de FFMPEG.
- [ffmpeg-python] pour l'utilisation de la librairie python pour FFMPEG.

## Utilisation

Cette application est un web service définit dans `app.py`. Il utilise la configuration du fichier `app.ini` avec notamment l'hôte et le port.

Pour lancer le serveur :

```bash
./app.py
```

### Routes

Le serveur utilise deux routes :
- `/` pour l'index.
- `/ffmpeg` pour utiliser FFMPEG. **Méthode POST nécessitant un JSON**

Concernant le JSON de l'action pour FFMPEG, il est défini ainsi :
```json
{
"method":"METHOD_FFMPEG",
"input":"FICHIER_SOURCE",
"output":"FICHIER_DESTINATION" // Optionnel
}
```

## Demo

Le fichier `demo.sh` contient les requêtes SHELL à utiliser pour prouver le fonctionnement des deux routes.


[FFMPEG]: https://www.ffmpeg.org/
[ffmpeg-python]: https://github.com/kkroening/ffmpeg-python
