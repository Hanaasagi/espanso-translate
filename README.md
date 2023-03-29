# espanso-translate

Translate English to other language.

https://user-images.githubusercontent.com/9482395/228575001-cff826eb-bd9b-4c85-8e57-69eed55b2960.mp4

### Installation

```
$ pip install openai
$ espanso install --external espanso-translate --git git@github.com:Hanaasagi/espanso-translate.git
```

### Config

```YAML
global_vars:
  # Your open-ai key
  - name: "OPENAI_KEY"
    type: "echo"
    params:
      echo: "<YOU KEY>"
  - name: "AI_MODEL"
    type: "echo"
    params:
      echo: "gpt-3.5-turbo"
  # Translate to what?
  - name: "DEST_LANG"
    type: "echo"
    params:
      echo: "Japanese"
  # Please don't change this
  - name: "SCRIPT_PATH"
    type: "echo"
    params:
      echo: '"$CONFIG/match/packages/espanso-translate/scripts/trans.py"'
  # Custom Python path for venv user
  - name: "PYTHON"
    type: "echo"
    params:
      echo: "<YOUR PYTHON PATH>"
```
