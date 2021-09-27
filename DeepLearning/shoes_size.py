import tensorflow as TF
import tensorflow.keras as TFKE




SHOES_SIZE = 260
USER_HEIGHT = 180
VAR_1 = TF.Variable(0.1)
VAR_2 = TF.Variable(0.1)

def LOSS_FUNC():
    return TF.square(SHOES_SIZE - (USER_HEIGHT * VAR_1 + VAR_2))

OPTION = TFKE.optimizers.Adam(learning_rate = 0.1)
for COUNT in range(3000):
    BEFORE_VAR_1 = VAR_1.numpy()
    BEFORE_VAR_2 = VAR_2.numpy()

    OPTION.minimize(LOSS_FUNC, var_list = [VAR_1, VAR_2])
    print(f"VAR_1 == {VAR_1.numpy()}\nVAR_2 == {VAR_2.numpy()}")

    AFTER_VAR_1 = VAR_1.numpy()
    AFTER_VAR_2 = VAR_2.numpy()

    if AFTER_VAR_1 == BEFORE_VAR_1 and AFTER_VAR_2 == BEFORE_VAR_2:
        break
        # pass

print(f"==============================FINALL VAR==============================\nVAR_1 == {VAR_1.numpy()}\nVAR_2 == {VAR_2.numpy()}")

print(USER_HEIGHT * VAR_1.numpy() + VAR_2.numpy())


# VAR_1 == 1.4364640712738037
# VAR_2 == 1.4364640712738037