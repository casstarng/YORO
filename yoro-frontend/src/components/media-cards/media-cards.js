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
    minWidth: 1000,
    maxWidth: 1500
  }
});

export default function ImgMediaCard() {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="530"
          image="/static/images/cards/contemplative-reptile.jpg"
        />
      </CardActionArea>
      <CardActions>
        <Button size="small" color="primary">
          Manual Recognization
        </Button>
      </CardActions>
    </Card>
  );
}
