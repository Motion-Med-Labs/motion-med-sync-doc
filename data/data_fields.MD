Below are the **Menstrual Cycle Tracking (MCT) Summaries** response fields from Garmin’s Women’s Health API, formatted as Markdown tables. The first table covers the top-level fields; the second table covers the **pregnancySnapshot** object (only present if the user is in a pregnant phase), and the third table covers the structure of each item in the **bloodGlucoseList** array.

---

## MCT Summary Fields

| **Property**                 | **Type** | **Description**                                                                                                                                        |
| ---------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **summaryId**                | string   | Unique identifier for the summary.                                                                                                                     |
| **periodStartDate**          | string   | The calendar date representing the period start date (format `yyyy-mm-dd`).                                                                            |
| **dayInCycle**               | integer  | The nth day in the user’s current cycle.                                                                                                               |
| **periodLength**             | integer  | Number of days indicating how long a period usually lasts.                                                                                             |
| **currentPhase**             | integer  | Indicates the phase in this cycle numerically (e.g., menstruation, fertile, etc.).                                                                     |
| **currentPhaseType**         | string   | Indicates the phase in this cycle as a string (e.g., `MENSTRUAL`, `FERTILE`, `FIRST_TRIMESTER`, etc.).                                                 |
| **lengthOfCurrentPhase**     | integer  | The length of the current phase in days.                                                                                                               |
| **daysUntilNextPhase**       | integer  | Number of days remaining until the next predicted phase.                                                                                               |
| **predictedCycleLength**     | integer  | Number of days predicted for the current cycle length.                                                                                                 |
| **isPredictedCycle**         | boolean  | `true` if this summary is a predicted cycle; `false` otherwise.                                                                                        |
| **cycleLength**              | integer  | The user-logged cycle length.                                                                                                                          |
| **lastUpdatedTimeInSeconds** | integer  | The UTC timestamp (in seconds) showing when a user last logged or updated their cycle information.                                                     |
| **hasSpecifiedCycleLength**  | boolean  | `true` if the user explicitly entered a cycle length in Garmin Connect; `false` otherwise.                                                             |
| **hasSpecifiedPeriodLength** | boolean  | `true` if the user explicitly entered a period length in Garmin Connect; `false` otherwise.                                                            |
| **pregnancySnapshot**        | object   | JSON object containing pregnancy information if the user is in a pregnant phase. This object is empty (`{}`) if the user is _not_ in a pregnant phase. |

---

## pregnancySnapshot Fields

If the user is in a pregnant phase, the `pregnancySnapshot` object will be populated with the following properties:

| **Property**                | **Type**   | **Description**                                                                                                                                   |
| --------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **title**                   | string     | Title or name assigned to the pregnancy (e.g., "Pregnancy 2021").                                                                                 |
| **originalDueDate**         | string     | The originally entered due date (`yyyy-mm-dd`).                                                                                                   |
| **dueDate**                 | string     | The updated due date, if applicable (`yyyy-mm-dd`).                                                                                               |
| **pregnancyCycleStartDate** | string     | The calendar date representing the start of the pregnancy cycle (`yyyy-mm-dd`).                                                                   |
| **numOfBabies**             | string     | A string representing the number of babies (e.g., `SINGLE`, `TWINS`).                                                                             |
| **weightGoalUserInput**     | dictionary | Contains `heightInCentimeters` (integer) and `weightInGrams` (integer), as entered by the user when they mark themselves as pregnant.             |
| **bloodGlucoseList**        | array      | An array of blood glucose measurements that the user has logged. See **Blood Glucose List Fields** (below) for the structure of each measurement. |

---

## Blood Glucose List Fields

Each entry in the `bloodGlucoseList` array is a dictionary with these properties:

| **Property**                      | **Type** | **Description**                                                                                       |
| --------------------------------- | -------- | ----------------------------------------------------------------------------------------------------- |
| **valueInMilligramsPerDeciliter** | float    | The numeric blood glucose reading in mg/dL.                                                           |
| **logType**                       | string   | The context or timing of the glucose reading (e.g., `BEFOREMEAL`, `AFTERMEAL`, `BEFOREBED`, `OTHER`). |
| **reportTimestampInSeconds**      | integer  | UTC timestamp (in seconds) indicating when the reading was logged.                                    |

---

**Note:**

- If the user is _not_ in a pregnant phase, `pregnancySnapshot` is simply an empty object (`{}`), and there is no `bloodGlucoseList`.
- The fields `fertileWindowStart` and `lengthOfFertileWindow` appear in some of Garmin’s examples. They may or may not appear depending on whether the user logs or predicts a fertile window. You can handle them similarly to other integer fields if they appear in your data.
