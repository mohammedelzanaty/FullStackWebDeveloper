import { SET_GOAL } from "../constants/action-types";

const INITIAL_STATE = {
  allSkiDays: [
    {
      resort: "Kirkwood",
      date: "2016-12-7",
      powder: true,
      backcountry: false
    },
    {
      resort: "Squaw Valley",
      date: "2016-12-8",
      powder: false,
      backcountry: false
    },
    {
      resort: "Mt Tallac",
      date: "2016-12-9",
      powder: false,
      backcountry: true
    }
  ],
  goal: 10,
  errors: [],
  resortNames: {
    fetching: false,
    suggestions: ["Squaw Valley", "Snowbird", "Stowe", "Steamboat"]
  }
};

const rootReducer = (state = INITIAL_STATE, action) => {
  if (action.type === SET_GOAL) {
    return { goal: action.payload };
  }
  return state;
};

export default rootReducer;