# Using Outscale Object Storage with Python

This small example project shows how to use [OOS](https://docs.outscale.com/en/userguide/OUTSCALE-Object-Storage-(OOS).html) using standard [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library.

Running this example will:
- Create a Bucket with a random name
- Put a string inside an object inside the bucket
- Read back that object
- Delete the object
- Delete the bucket

# Pre-requisites

You will need:
- python3 and preferably virtualenv installed
- An [Access Key and Secret Key](https://docs.outscale.com/en/userguide/About-Access-Keys.html)

# Running the example

1. (optional) Setup your virtual env:
```bash
virtualenv -p python3 .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Setup your credentials and region:

```bash
export OSC_REGION="eu-west-2"
export OSC_ACCESS_KEY="MyAccessKey"
export OSC_SECRET_KEY="MySecretKey"
```

4. Run the example:

```bash
> python src/main.py
```

You should have a  similar output:
```bash
> python src/main.py
creating private bucket named bucket-test-voxa...
bucket bucket-test-voxa created
writing 'Hello World' to public my-data object...
writed to bucket-test-voxa object
reading my-data object...
read object ok: b'Hello World'
deleting my-data object...
deleted my-data object
deleting bucket named bucket-test-voxa...
bucket bucket-test-voxa delete
```

Check [main.py](src/main.py) to see how it is done.

# Contribution guidelines

Feel free to open an issue for discussion or bug report.

# License

> Copyright Outscale SAS
>
> BSD-3-Clause