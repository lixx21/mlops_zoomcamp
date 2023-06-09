import wandb

# Always initialize a W&B run to start tracking
wandb.init()

# (Optional) Declare an upstream dataset dependency
# see the `Declare Dataset Dependency` tab for
# alternative examples.
dataset = wandb.use_artifact("mnist:latest")

# At the end of every epoch (or at the end of your script)...
# ... Serialize your model
model.save("path/to/model.pt")
# ... Create a Model Version
art = wandb.Artifact(f'mnist-nn-{wandb.run.id}', type="model")
# ... Add the serialized files
art.add_file("path/to/model.pt", "model.pt")
# (optional) Log training metrics
wandb.log({"train_loss": 0.345, "val_loss": 0.456})
# ... Log the Version
if model_is_best:
    # If the model is the best model so far,
    #  add "best" to the aliases
    wandb.log_artifact(art, aliases=["latest", "best"])
else:
    wandb.log_artifact(art)