# storagebot

### Payment 
To get payment work follow these steps: 
1. Go to BotFather
1. Choose your bot which should process payments
1. Choose Payments option from the list
1. Add a payment provider which you want to use - Yokassa in this case.
1. Choose the Test option
1. You will be redirected to a provider bot, follow the next steps described there.
1. Once you retrieved a test token from the provider, place it in your ``.env`` file, like:
```
YOOKASSA_TEST_TOKEN=472824612:TEST:56225
```