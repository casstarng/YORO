import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";
import Button from "@material-ui/core/Button";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles({
  card: {
    Width: "100%"
  },
  media: {
    height: 440
  }
});
const ProfileDisplay = props => {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardActionArea>
        <CardMedia
          className={classes.media}
          image={props.person.profile_pic}
          title="Contemplative Reptile"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="h2">
            {props.person.first_name + " " + props.person.last_name}
          </Typography>
          <Typography variant="body2" color="textSecondary" component="p">
            Attendee
          </Typography>
        </CardContent>
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          Accept
        </Button>
        <Button size="small" color="primary">
          Reject
        </Button>
      </CardActions>
    </Card>
  );
};
export default ProfileDisplay;
