   import xgboost as xgb
   
   # Train the model
   dtrain = xgb.DMatrix(X_train, label=y_train)
   params = {'objective': 'binary:logistic'}
   bst = xgb.train(params, dtrain)
   
   # Get predictions
   class_labels = bst.predict(dtest) > 0.5  # Default threshold for binary classification
   
   # Get probability estimates
   probability_estimates = bst.predict(dtest)  # Raw probability scores
   