# Bull and Bear Project

## First Pass

### Account management
- [x] login
- [x] logout
- [ ] update password
- [ ] account/profile page

### Prediction backend
- [x] outcomes have probabilities/odds
- [x] prediction model
- [x] url/view to wager 1.0 on a prediction
- [x] prediction view checks and subtracts reputation
- [x] prediction updates odds
- [ ] url/view to determine an event
- [x] users have prediction currency
- [x] users have reputation

### Prediction frontend
- [x] button/link to wager on an outcome
- [x] profile shows reputation
- [x] events/outcomes show predictions
- [x] header with user info

to run locally:

python3 manage.py \<command\> --settings'bull_bear.local_settings'
