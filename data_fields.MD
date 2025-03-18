# Activity Fields

# Health Fields

# Training Fields

# Menstrual Cycle Tracking (MCT) Fields

| Property                 | Type    | Description                                                                              |
| ------------------------ | ------- | ---------------------------------------------------------------------------------------- |
| summaryId                | string  | Unique identifier for the summary                                                        |
| periodStartDate          | string  | The calendar date representing period start date. The date format is 'yyyy-mm-dd'        |
| dayInCycle               | integer | Represents nth day in cycle                                                              |
| periodLength             | integer | Number of days indicating how long a period usually last                                 |
| currentPhase             | integer | Indicates the phase in this cycle like menstruation, fertile, etc.,                      |
| currentPhaseType         | String  | Indicates the phase in this cycle.                                                       |
| lengthOfCurrentPhase     | integer | Represents the length of current phase in days                                           |
| daysUntilNextPhase       | integer | Number of days remaining to reach the next predicted phase                               |
| predictedCycleLength     | integer | Number of days predicted to be the current cycle length                                  |
| isPredictedCycle         | boolean | A boolean to show if this summary is a predicted cycle or not                            |
| cycleLength              | integer | A user logged cycle length                                                               |
| lastUpdatedTimeInSeconds | integer | Time in seconds showing when a user logged their symptoms                                |
| hasSpecifiedCycleLength  | boolean | A boolean to show if cycle lenght was provided by the user through Garmin Connect        |
| hasSpecifiedPeriodLength | boolean | A boolean to show if period length value was provided by the user through Garmin Connect |

If a user is in a pregnant phase, the pregnancySnapshot field will be populated with the following fields:

| Property                | Type       | Description                                                                                                                                                                                                                                     |
| ----------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| title                   | String     | Title used for the user's pregnancy                                                                                                                                                                                                             |
| originalDueDate         | String     | The calendar date representing the user's original due date entered by the user                                                                                                                                                                 |
| dueDate                 | String     | The calendar date representing an updated due date. This value is entered by the user in Garmin Connect.                                                                                                                                        |
| pregnancyCycleStartDate | String     | The calendar date representing the start of the user's pregnancy cycle                                                                                                                                                                          |
| numOfBabies             | String     | A string representing the number of babies during the user's pregnancy                                                                                                                                                                          |
| weightGoalUserInput     | Dictionary | A representation of the user's height in centimeters (heightInCentimeters) and weight in grams (weightInGrams). This is entered by the user when the user is marked as pregnant in Garmin Connect. Please see below example for data structure. |
| bloodGlucoseList        | Dictionary | A representation of the user-logged blood glucose readings. This contains valueInMilligramsPerDeciliter (floating point), logType (String), and reportTimestampInSeconds (integer). Please see below example for data structure.                |
