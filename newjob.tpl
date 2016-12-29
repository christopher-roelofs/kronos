<!DOCTYPE html>
<html>
<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<body>

<form action="/createjob" method="post">
  <div class="form-group">
    <label for="name">Name:</label>
    <input type="text" class="form-control"  name="name">
  </div>
  <div class="form-group">
    <label for="group">Group:</label>
    <input type="text" class="form-control"  name="group">
  </div>
  <div class="form-group">
    <label for="description">Description</label>
    <textarea type=text class="form-control"   name="description" rows="3"></textarea>
  </div>
  <div class="form-group">
    <label for="xml">XML Properties</label>
    <textarea  type=text class="form-control"  name="xml" rows="10"></textarea>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>


</body>